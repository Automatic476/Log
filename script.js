async function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: 36.0726, lng: -79.7920 } // Centered on Guilford County
    });

    try {
        // Fetch network data
        const response = await fetch('network_data.json');
        const data = await response.json();

        // Plot markers for network data
        data.forEach(record => {
            // Source IP marker
            new google.maps.Marker({
                position: { lat: record.src_lat, lng: record.src_lng },
                map: map,
                title: `Src IP: ${record.src_ip}`
            });

            // Destination IP marker
            new google.maps.Marker({
                position: { lat: record.dst_lat, lng: record.dst_lng },
                map: map,
                title: `Dst IP: ${record.dst_ip}`
            });
        });
    } catch (error) {
        console.error('Error initializing map:', error);
    }
}

window.onload = initMap;
