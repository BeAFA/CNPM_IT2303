function addToCart(id,name,price){
    fetch("api/carts",{
        method: "post",
        body: JSON.stringify({
            "id":id,
            "name":name,
            "price":price
        }),
        headers:{
            "content-type": "application/json"
        }
    }).then(res => res.json()).then(data => {
        let c = document.getElementsByClassName('cart-counter');
        for(let e of c){
            e.innerText = data.total_quantity;
        }
    })
}

function updateCart(productId, obj){
    fetch(`api/carts/${productId}`,{
        method: "put",
        body: JSON.stringify({
            "quantity": parseInt(obj.value)
        }),
        headers:{
            "content-type": "application/json"
        }
    }).then(res => res.json()).then(data => {
        let c = document.getElementsByClassName('cart-counter');
        let p = document.getElementsByClassName('cart-total-price');
        for(let e of c){
            e.innerText = data.total_quantity;
        }for(let e of p){
            e.innerText = data.total_amount.toLocaleString("en");
        }

    })
}

function deleteProduct(productId){
    if(confirm("Bạn có chắc chắn muốn xóa sản phẩm không?") ===true){
        fetch(`api/carts/${productId}`,{
            method: "delete",
            headers:{
                "content-type": "application/json"
            }
        }).then(res => res.json()).then(data => {
            let c = document.getElementsByClassName('cart-counter');
            let p = document.getElementsByClassName('cart-total-price');
            let i = document.getElementById(`product${productId}`);
            for(let e of c){
                e.innerText = data.total_quantity;
            }for(let e of p){
                e.innerText = data.total_amount.toLocaleString("en") + " VNĐ";
            }
            i.style.display = "none";
        })
    }
}

function pay(){
    if(confirm("Xác nhận thanh toán?") ===true){
        fetch("api/pay",{
            method: "post",
        }).then(res => res.json()).then(data => {
            if(data.status===200){
                location.reload();
            }else{
                alert(data.err_msg);
            }
        })
    }
}