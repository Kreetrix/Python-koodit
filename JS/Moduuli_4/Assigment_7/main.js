'use strict';

const sub_key = ''; //insert the subscription key here!

// show the map
const map = L.map('map').setView([60.1785553, 24.8786212], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const apiAddress = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'; // cors issues may arise, use proxy or browser plugin if necessary

const form = document.querySelector('#form');

//format millis
function Time(duration) {
    let seconds = Math.floor((duration / 1000) % 60),
        minutes = Math.floor((duration / (1000 * 60)) % 60),
        hours = Math.floor((duration / (1000 * 60 * 60)) % 24);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    return hours + ":" + minutes + ":" + seconds
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = form.querySelector('#start');
    let value = input.value;

    let res = await fetch(`https://api.digitransit.fi/geocoding/v1/search?digitransit-subscription-key=${sub_key}&text=${value}&size=1`)
    res = await res.json()
    let coordinates = res.features[0].geometry.coordinates
    console.log(coordinates)

    let trip = await getRoute({latitude: coordinates[1], longitude: coordinates[0]}, {latitude: 60.223876, longitude: 24.758061})
    console.log(trip)
    const trip_s = document.querySelector("#st");
    const trip_start = document.createTextNode(Time(trip[0].startTime));
    trip_s.appendChild(trip_start);
    const trip_e = document.querySelector("#end");
    const trip_end = document.createTextNode(Time(trip[trip.length - 1].endTime));
    trip_e.appendChild(trip_end);
})


async function getRoute(origin, target) {
    const GQLQuery = `{
      plan(
        from: {lat: ${origin.latitude}, lon: ${origin.longitude}}
        to: {lat: ${target.latitude}, lon: ${target.longitude}}
        numItineraries: 1
      ) {
        itineraries {
          legs {
            startTime
            endTime
            mode
            duration
            distance
            legGeometry {
              points
            }
          }
        }
      }
    }`;

    const fetchOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'digitransit-subscription-key': sub_key,
        },
        body: JSON.stringify({query: GQLQuery}),
    };

    let trip = await fetch(apiAddress, fetchOptions)
        .then(function (response) {
            return response.json();
        })
        .then(function (result) {
            const googleEncodedRoute = result.data.plan.itineraries[0].legs;
            for (let i = 0; i < googleEncodedRoute.length; i++) {
                let color = '';
                switch (googleEncodedRoute[i].mode) {
                    case 'WALK':
                        color = 'green';
                        break;
                    case 'BUS':
                        color = 'red';
                        break;
                    case 'RAIL':
                        color = 'cyan'
                        break;
                    case 'TRAM':
                        color = 'magenta'
                        break;
                    default:
                        color = 'blue';
                        break;
                }
                const route = (googleEncodedRoute[i].legGeometry.points);
                const pointObjects = L.Polyline.fromEncoded(route).getLatLngs(); // fromEncoded: convert Google encoding to Leaflet polylines
                L.polyline(pointObjects).setStyle({
                    color
                }).addTo(map);
            }
            map.fitBounds([[origin.latitude, origin.longitude], [target.latitude, target.longitude]]);
            return result.data.plan.itineraries[0];
        })
        .catch(function (e) {
            console.error(e.message);
        });
    return trip.legs;
}
