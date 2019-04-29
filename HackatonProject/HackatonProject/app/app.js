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
        markers: [],
        loginUser: {},
        newUser: {},
        newProduct: {},
        misOrdenes: {},
        center: {
            lat: 23.634501,
            lng: -102.55278399999997

        },
        MapZoom:4,
        apiPath: 'http://hdigitalbc.pythonanywhere.com/api/',
        currentPlace: {},
        currentUser: {},
        products: {}
    },
    created: function () {
        $(document).ready(function () {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
            $('select').formSelect();
            $('.collapsible').collapsible();
           
        });
        if (window.location.pathname == '/Home/MapaDeBusqueda') {
            this.getProducts();
        }

        this.currentUser = this.$session.get('currentUser');
        //this.$session.set('username', "kass"); // Set the username in session Storage
        //this.$session.set('username', "tu"); // Set the username in session Storage

    },

    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('');
        },
        login: function () {       

            axios({
                method: 'post',
                url: this.apiPath + "login/",
                headers: { 'Content-Type': 'application/json'},
                data: {
                    username: this.loginUser.email,
                    password: this.loginUser.password
                }
            }).then(response => {
                this.info = response.data;
                this.$session.set('currentUser', response.data); // Set the username in session Storage
                window.location.href = 'home/MapaDeBusqueda';
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
                this.newUser.lat = this.center.lat;
                this.newUser.lon = this.center.lng;
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
        },
        getProducts: function () {
            axios({
                method: 'get',
                url: this.apiPath + "get_products/",
                headers: { 'Content-Type': 'application/json' }
            }).then(response => {
                this.products = response.data;
                console.log(response.data);
                for (var i = 0; i < this.productslength; i++) {
                    this.productCenter = {
                        lat: this.products.inventory_id.user_id.pos_lat,
                        lng: this.products.inventory_id.user_id.pos_lon
                    };
                    this.markers.push({ position: this.productCenter });

                }
            })
                .catch(error => {
                    console.log(error);
                    this.errored = true;
                });
        },

        signUp: function () {
            axios({
                method: 'post',
                url: this.apiPath + "setup_user/",
                headers: { 'Content-Type': 'application/json' },
                data: {
                    username: this.newUser.username,
                    password: this.newUser.password,
                    commercial_name: this.newUser.comercialname,
                    city: this.newUser.city,
                    state: this.newUser.state,
                    district: this.newUser.district,
                    postal_code: this.newUser.cp,
                    shipping_notes: this.newUser.notes,
                    pos_lat: this.newUser.lat,
                    pos_lon: this.newUser.lon

                }
            }).then(response => {
                this.info = response.data;
                M.toast({ html: 'A sido registrado correctamente' });
                window.location.href = 'home/';
            })
                .catch(error => {
                    console.log(error);
                    this.errored = true;
                });
        },

        AgregarEquipo: function () {
            axios({
                method: 'post',
                url: this.apiPath + "add_product/",
                headers: { 'Content-Type': 'application/json' },
                data: {
                    name: this.newProduct.nombreComercial,
                    description: this.newProduct.descripcion,
                    user_id: this.currentUser.id,
                    price: this.newProduct.precio,
                    quantity: this.newProduct.cantidad
                }
            }).then(response => {
                this.info = response.data;
                M.toast({ html: 'Equipo agregado' });
            })
                .catch(error => {
                    console.log(error);
                    this.errored = true;
                });
        },

        Ordenes: function () {
            axios({
                method: 'post',
                url: this.apiPath + "get_products/",
                headers: { 'Content-Type': 'application/json' },
                data: {
                    
                    user_id: this.currentUser.id

                }
            }).then(response => {
                this.product_id = response.data;
               
            })
                .catch(error => {
                    console.log(error);
                    this.errored = true;
                });
        },
        setProductLocation: function (product) {
            this.center = {
                lat: product.inventory_id.user_id.pos_lat,
                lng: product.inventory_id.user_id.pos_lon,
            };
            this.MapZoom = 12;
        }


    }
});