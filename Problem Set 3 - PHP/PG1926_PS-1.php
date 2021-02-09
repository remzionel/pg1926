<?php

date_default_timezone_set('Europe/Istanbul');

$zaman = time();

echo 'Saat: '.date('H:i', $zaman).'<br>';

$saat = date('H', $zaman);

if($saat >= 06 && $saat < 10){ // Saat 06:00 - 10:00 arası
    echo 'Günaydın';
}elseif($saat >= 10 && $saat < 17){ // Saat 10:00 - 17:00 arası
    echo 'İyi Günler';
}elseif($saat >= 17 && $saat < 20){ // Saat 17:00 - 20:00 arası
    echo 'İyi Akşamlar';
}elseif($saat >= 20 && $saat < 24){ // Saat 20:00 - 00:00 arası
    echo 'İyi Geceler';
}elseif($saat >= 00 && $saat < 06){ // Saat 00:00 - 06:00 arası
    echo 'Esenlikler Dilerim';
}

?>