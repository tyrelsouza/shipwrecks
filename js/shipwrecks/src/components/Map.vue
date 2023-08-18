<template>
  <div class="map-container">
    <div ref="map" class="map"></div>
  </div>
</template>

<script>

import mapboxgl from 'mapbox-gl';
import axios from 'axios';
const ACCESS = 'pk.eyJ1IjoidHlyZWxzb3V6YSIsImEiOiJjbGxnMWJuYmcwczZwM3JxaGxhemJrb3hvIn0.89kO6J8e--lyQSm_lWaBLw';

export default {
  data() {
    return {
      map: null,
      shipwrecks: [],
    };
  },
  mounted() {
      this.fetchShipwrecks();
  },
  methods: {
    async fetchShipwrecks() {
      try {
        const response = await axios.get('http://localhost:5000/api/shipwrecks');
        this.shipwrecks = response.data;

        this.drawMapWithMarkers();
      } catch (error) {
        console.error('Error fetching shipwrecks:', error);
      }
    },
    drawMapWithMarkers() {
      mapboxgl.accessToken = ACCESS;

      this.map = new mapboxgl.Map({
        container: this.$refs.map,
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [-78.968,35.916],
        zoom: 7
      });

      this.map.on('load', () => {
        new mapboxgl.Marker().setLngLat([-78.968,35.916]).addTo(this.map)
         
        this.shipwrecks.forEach(shipwreck => {
          const coordinates = shipwreck.coordinates;
          if (coordinates && coordinates.length === 2) {
            new mapboxgl.Marker().setLngLat({ lng: coordinates[0], lat: coordinates[1] }).addTo(this.map);
          }
        });
      });


    }
  },
  beforeDestroy() {
    if (this.map) {
      this.map.remove();
    }
  }
};
</script>
<style>
.map-container {
  position: relative;
  height: 400px;
}

.map {
  width: 100%;
  height: 100vh;
}
</style>
