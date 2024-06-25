const btnCarro = document.querySelector('.container-carro-icon');
const containerCarroProductos = document.querySelector('.containter-carro-productos');

btnCarro.addEventListener('click', () => {
    containerCarroProductos.classList.toggle('carro-oculto');
});

const carroInfo = document.querySelector('.carro-producto');
const rowProducto = document.querySelector('.row-producto');

const productosLista = document.querySelector('.container-items');

// Variables
let allProducts = [];
const valorTotal = document.querySelector('.valor-total');
const countProductos = document.querySelector('#contador-productos');
const carroVacio = document.querySelector('.carro-vacio');
const carroTotal = document.querySelector('.carro-total');

productosLista.addEventListener('click', e => {
    if (e.target.classList.contains('btn-anadir-productos')) {
        const producto = e.target.parentElement;

        const productoInfo = {
            cantidad: 1,
            nombre: producto.querySelector('h2').textContent,
            nombre2: JSON.parse(nombre),
            precio: producto.querySelector('p').textContent,
        };

        const exits = allProducts.some(producto => producto.nombre === productoInfo.nombre);

        if (exits) {
            const productos = allProducts.map(producto => {
                if (producto.nombre === productoInfo.nombre) {
                    producto.cantidad++;
                    return producto
                } else {
                    return producto
                }
            });
            allProducts = [...productos];
        } else {
            allProducts = [...allProducts, productoInfo]
        }

        showHTML();
        console.log(nombre2)
        console.log(productosLista);
    };
});

rowProducto.addEventListener('click', e => {
    if (e.target.classList.contains('icon-close')) {
        const producto = e.target.parentElement;
        const nombre = producto.querySelector('p').textContent;

        allProducts = allProducts.filter(
            producto => producto.nombre !== nombre
        );

        console.log(allProducts);

        showHTML();
    };
});

// mostrar HTML

const showHTML = () => {
    if (!allProducts.length) {
        carroVacio.classList.remove('hidden');
        rowProducto.classList.add('hidden');
        carroTotal.classList.add('hidden');
    } else {
        carroVacio.classList.add('hidden');
        rowProducto.classList.remove('hidden');
        carroTotal.classList.remove('hidden');
    }

    rowProducto.innerHTML = '';

    let total = 0;
    let totalProductos = 0;

    allProducts.forEach(producto => {
        const containerProducto = document.createElement('div');
        containerProducto.classList.add('carro-producto');

        containerProducto.innerHTML = `
        <div class="carro-producto-info">
            <span class="carro-producto-cantidad">${producto.cantidad}</span>
            <p class="carro-producto-nombre">${producto.nombre}</p>
            <span class="carro-producto-precio">${producto.precio}</span>
        </div>
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="icon-close"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6 18L18 6M6 6l12 12"
            />
        </svg>
    `;
        rowProducto.append(containerProducto);

        total = total + parseInt(producto.cantidad * producto.precio.slice(1));
        totalProductos = totalProductos + producto.cantidad;
    });

    valorTotal.innerHTML = `$${total}`;
    countProductos.innerHTML = totalProductos;
};