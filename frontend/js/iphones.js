window.addEventListener('load', () => {
    const app = Vue.createApp({
        data() {
            return {
                iphones: [],
                iphone: {
                    IMEI: '',
                    modelo: '',
                    color: '',
                    gb: null,
                    bateria: null,
                    precio: null
                },
                isVisible: true,

                
            }
        },
        created() {
            this.listIphones();
        },
        methods: {

            
            listIphones: async function() {
                const res = await fetch('http://127.0.0.1:5000/iphones');
                const data = await res.json();
                console.log(data);
                this.iphones = data.iPhones;
            },
            deleteIphone: async function(imei) {
                const confirmation = confirm('¿Estás seguro de eliminar este iPhone?');
                if (confirmation) {
                    const res = await fetch(`http://127.0.0.1:5000/iphones/${imei}`, {
                        method: 'DELETE'
                    });
                    
                    if (res.ok) {
                        this.listIphones();
                    } else {
                        console.error('Error al eliminar el iPhone:', res.statusText);
                    }
                }
            },

            selectIphone: function(imei) {
                console.log('Seleccionando iPhone...');
                this.isVisible = false;
                const iphone = this.iphones.find(iphone => iphone.IMEI === imei);
                this.iphone = Object.assign({}, iphone);
                bateria = this.iphone.bateria;
                precio = this.iphone.precio;
                
            },
            updateIphone: async function(imei) {
                console.log('Actualizando iPhone...');
                
                const updatedData = {
                    bateria: this.iphone.bateria,
                    precio: this.iphone.precio
                };
                this.isVisible = true;
                const res = await fetch(`http://127.0.0.1:5000/iphones/${imei}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(updatedData)
                });
            
                if (res.ok) {
                    console.log('iPhone actualizado correctamente');
                    this.listIphones();
                    this.clean();
                } else {
                    const errorData = await res.json();
                    console.error('Error al actualizar el iPhone:', res.statusText, errorData);
                }
            },

            addIphone: async function(event) {
                if (this.isVisible == false) {
                    this.updateIphone(this.iphone.IMEI);
                } else {
                    console.log('Agregando iPhone...');
                    console.log(this.iphone);
                    const res = await fetch('http://127.0.0.1:5000/iphones', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(this.iphone)
                    });
                
                    if (res.ok) {
                        this.iphone = {
                            IMEI: '',
                            modelo: '',
                            color: '',
                            gb: 0,
                            bateria: null,
                            precio: null
                        };
                        this.listIphones();
                    } else {
                        const errorData = await res.json();
                        console.error('Error al agregar el iPhone:', res.statusText, errorData);
                    }
                }
                },
            

            clean: function(event) {
                this.iphone = {
                    IMEI: '',
                    modelo: '',
                    color: '',
                    gb: null,
                    bateria: null,
                    precio: null
                };
            }
        }
    });

    app.mount('#app');
});
