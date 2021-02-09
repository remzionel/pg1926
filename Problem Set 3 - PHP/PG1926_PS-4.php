<?php
$satisFiyati = 6.78;
if(isset($_POST['ajax']) && isset($_POST['sayi'])){
    function paraUstu($satisFiyati, $sayi){
        $banknotlar = [1, 0.50 , 0.25, 0.10, 0.05, 0.01];
        $paralar_tr = [
            '1'     => '1 Lira',
            '0.50'  => '50 Kuruş',
            '0.25'  => '25 Kuruş',
            '0.1'   => '10 Kuruş',
            '0.05'  => '5 Kuruş',
            '0.01'  => '1 Kuruş',
            '0'     => null
        ];
        $fark = round($sayi - $satisFiyati, 2);
        $paraUstu = [];
        $paraUstu_a = [];
        $asd = [];
        if($fark >= 0){ // Para üstü (fark) sıfırdan büyükse
            for($i=0; $i<count($banknotlar); $i++){ // banknotları döngüye alıyoruz
                $asd[] = $fark.'--'.$banknotlar[$i];
                while($fark >= $banknotlar[$i]){ // fark sıradaki banknottan büyükse
                    $asd[] = $fark.'--'.$banknotlar[$i]; // sıradaki banknotu array içine alıyoruz
                    $paraUstu_a[] = (string) $banknotlar[$i]; // sıradaki banknotu array içine alıyoruz
                    $fark = round($fark - $banknotlar[$i], 2); // farktan sıradaki banknotu çıkarıp döngüyü başa alıyoruz
                }
            }
            $paraUstu_cv = array_count_values($paraUstu_a);
            foreach($paraUstu_cv as $anahtar => $deger){
                $paraUstu[] = $deger.' adet '. $paralar_tr[$anahtar];
            }
            return 'Para Üstü: '.round($sayi - $satisFiyati, 2).' TL olup; '.implode(', ', $paraUstu).' olarak müşteriye verilir.';
        }else{
            return 'Para Üstü Yok.';
        }
    }
    $sayi = (float) $_POST['sayi'];
    if($sayi<$satisFiyati){
        die('Teklif, Satış Fiyatından Küçük Olamaz.');
    }elseif($sayi){
        die(paraUstu($satisFiyati, $sayi));
    }else{
        die($_POST['sayi'].' Bir Sayı Değil. Şansını Zorlama Bence :)');
    }
}
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Para Üstü</title>
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
    <h1 class="baslik">Para Üstü</h1>
    <h4 class="baslik">Satış Fiyatı: <?=$satisFiyati;?></h4>
    <input type="number" class="input" placeholder="Fiyat Teklifi Giriniz"/>
    <br>
    <button type="button" class="buton" onClick="ajax();" min="<?=$satisFiyati;?>">Kontrol Et</button>
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