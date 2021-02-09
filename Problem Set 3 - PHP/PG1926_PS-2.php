<?php

if(isset($_POST['ajax']) && isset($_POST['sayi'])){
    function MSKontrol($sayi){
        $topla = 0;
        for ($i=1; $i<$sayi; $i++){
            if($sayi%$i == 0){
                $topla = $topla + $i;
            }
        }
        return $topla == $sayi;
    }
    $sayi = (int) $_POST['sayi'];
    if($sayi){
        if(MSKontrol($_POST['sayi'])){
            die($_POST['sayi'].' Mükemmel Sayıdır.');
        }else{
            die($_POST['sayi'].' Mükemmel Sayı Değildir.');
        }
    }else{
        die($_POST['sayi'].' Bir Sayı Değil. Şansını Zorlama Bence :)');
    }
}
?> 
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Mükemmel Sayı</title>
    <style>
        body {
            text-align: center;
        }
        .baslik {
            color: #000;
        }
        .input {
            border: 3px solid #1f212d;
            color: #1f212d;
            padding: 10px 15px;
            text-align: center;
            font-size: 25px;
            margin-bottom: 15px;
        }
        .buton {
            background-color: #1f212d;
            border: none;
            color: #fff;
            padding: 10px 15px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 15px;
        }
    </style>
</head>


<body>
    <h1 class="baslik">Mükemmel Sayı</h1>
    <input type="number" class="input" placeholder="Sayı Giriniz"/>
    <br>
    <button type="button" class="buton" onClick="ajax();">Kontrol Et</button>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script>
        function ajax(){
            var veriler = {
                ajax: true, 
                sayi: $('.input').val()
            };
            $.ajax({
                url: '<?=basename($_SERVER['REQUEST_URI']);?>',
                type: 'POST',
                data: veriler,
                error: function(xhr, errorString, exception) {
                    console.log(xhr, errorString, exception);
                },
                success: function(cevap) {
                    console.log(cevap);
                    alert(cevap);
                    $('.input').val('')
                }
            });
        }
    </script>
</body>
</html>