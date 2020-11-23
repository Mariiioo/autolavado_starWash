// ARCHIVO PARA GUARDAR SOBRE EL CACHE
var CACHE_NAME = 'my-site-cache-v1'; // NOMBRE DONDE SE CARGARAN TODOS CACHE
// TODO LO QUE SE QUIERA GUARDAR
var urlsToCache = [
    '/', // CARGARA PAGINA INDEX
    '/galeria/', // CARGARA PAGINA GALERIA
    '/conocenos/', // CARGARA PAGINA MISION Y VISION
    '/static/css/estilos.css', // ESTILOS
    '/static/css/ligthbox.min.css', // ESTILOS
    '/static/img/logo/Logo.png', //IMAGENES
    '/static/img/IconosGaleria/next.png', //ICONOS DE GALERIA
    '/static/img/IconosGaleria/prev.png', //ICONOS DE GALERIA
];

// LISTENERS

self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME) // Abrira y crea el cache con el nombre dado
        .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache); // AGREGA TODO LAS URL INDICADAS
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return fetch(event.request)
                .catch(function(rsp) {
                    return response;
                });
        })
    );
});