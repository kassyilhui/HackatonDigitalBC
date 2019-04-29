Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyB0ualSPp-6O-QxrnHyc4CwzMPIufKzRmQ',
        v: '3.26',
        libraries: 'places'
    },
    // Demonstrating how we can customize the name of the components
    installComponents: true

});
Vue.use(VueSessionStorage);
var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!',
        mainUrl: '',
        markers:[],
        center: {
            lat: 23.634501,
            lng: -102.55278399999997

        },
        MapZoom:4,
        apiPath: 'http://hdigitalbc.pythonanywhere.com/api/',
        currentPlace: {}
    },
    created: function () {
        $(document).ready(function () {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
            $('select').formSelect();
            $('.collapsible').collapsible();
        });
        //this.$session.set('username', "kass"); // Set the username in session Storage
        //this.$session.set('username', "tu"); // Set the username in session Storage

    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('');
        },
        login: function () {
            var data = {
                "username": "jesus96",
                "password": "123456"
            };

            axios({
                method: 'post',
                url: this.apiPath + "login/",
                headers: { 'Content-Type': 'application/json'},
                data: {
                    username: "jesus96",
                    password: "123456"
                }
            }).then(response => {
                this.info = response.data;
            })
                .catch(error => {
                    console.log(error);
                    this.errored = true;
                });
        },
        setPlace: function (place) {
            this.currentPlace = place;
        },
        addMarker: function () {
            if (this.currentPlace) {
                this.center = {
                    lat: this.currentPlace.geometry.location.lat(),
                    lng: this.currentPlace.geometry.location.lng(),
                };
               this.markers.push({ position: this.center });
                this.MapZoom = 12;
            }
        },
        centerCurrentPlace: function () {
            if (this.currentPlace) {
                this.center = {
                    lat: this.currentPlace.geometry.location.lat(),
                    lng: this.currentPlace.geometry.location.lng(),
                };
                this.MapZoom = 12;
            }
        }

    }
});