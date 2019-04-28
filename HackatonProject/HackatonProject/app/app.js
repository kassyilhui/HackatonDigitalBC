Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyB0ualSPp-6O-QxrnHyc4CwzMPIufKzRmQ',
        v: '3.26',
        libraries: 'places'
    },
    // Demonstrating how we can customize the name of the components
    installComponents: true

});

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!',
        mainUrl: '',
        center: {
            lat: 10.0,
            lng: 10.0
        },
        currentPlace: {}
    },
    created: function () {
        $(document).ready(function () {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
        });
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        },
        hola: function () {
            axios
                .get('/home/hola')
                .then(response => {
                    this.info = response.data.bpi
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                })
                .finally(() => this.loading = false)
        },
        setPlace(place) {
            this.currentPlace = place;
        },
        addMarker() {
            if (this.currentPlace) {
                this.center = {
                    lat: this.currentPlace.geometry.location.lat(),
                    lng: this.currentPlace.geometry.location.lng(),
                };
                
                this.currentPlace = null;
            }
        }
        
    }
})