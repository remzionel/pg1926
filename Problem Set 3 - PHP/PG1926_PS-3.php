<?php

if(isset($_POST['ajax']) && isset($_POST['sayi'])){
    function ASKontrol($sayi){
        $asal = true;
        $i = 2;
        while ($i < $sayi) {
            if ($sayi % $i == 0){
                $asal = false;
                break;
            }
            $i++;
        }
        return $asal;
    }
    $sayi = (int) $_POST['sayi'];
    if($sayi){
        if(ASKontrol($_POST['sayi'])){
            die($_POST['sayi'].' Asal Sayıdır.');
        }else{
            die($_POST['sayi'].' Asal Sayı Değildir.');
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
<title>Asal Sayı</title>
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
    <h1 class="baslik">Asal Sayı</h1>
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