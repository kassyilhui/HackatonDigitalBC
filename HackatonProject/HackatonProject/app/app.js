var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!',
        mainUrl: ''
    },
    created: function () {
        $(document).ready(function () {
            $('.sidenav').sidenav();
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
        }
    }
})