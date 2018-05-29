<?php
/**
 * @Author
 *  Jeong Han
 * @date
 *  8.April.2018
 * @ref
 *  http://blog.devez.net/292 - list of filename in diretory
 *  https://www.linkedin.com/learning/view-source/015-listing-files-on-a-directory-with-php - directory files rotator
 */


// 폴더명 지정
$dir = "./img";
 
// 핸들 획득
$handle  = opendir($dir);
 
$files = array();
 
// 디렉터리에 포함된 파일을 저장한다.
while (false !== ($filename = readdir($handle))) {
    if($filename == "." || $filename == ".."){
        continue;
    }
 
    // 파일인 경우만 목록에 추가한다.
    if(is_file($dir . "/" . $filename)){
        array_push($files,"<img src=\"img/".$filename."\"></br>"); // 배열에 img태그 내용 삽입
        $files[] = $dir."/".$filename;                             // 배열에 파일 경로 삽입
    }
}
 
// 핸들 해제 
closedir($handle);
 
// 정렬, 역순으로 정렬하려면 rsort 사용
sort($files);

// 배열 내용 모두 출력
echo "path_data</br>";
foreach($files as $data){
    echo $data;
    //echo json_encode($data);
    echo "</br>";
    //echo($data);
}


/**
 * @Author
 *  Jeong Han
 * @Date
 *  18.May.2018
 * @ref
 *  https://stackoverflow.com/questions/20538777/get-image-name-resolution-path-extension-and-fileszie
 * @memo
 *  image file meta_data
 */
/*
$files = glob("./img/*");

$metadatas = array();

for ($i = 0; $i < count($files); $i++) {
    $image = $files[$i];
    $path = pathinfo($image);
    $name = $path['filename']; //파일 이름
    $ext = $path['extension']; //확장자
    list($width, $height) = getimagesize($image);
    $resolution = $width . ' x ' . $height . ' Pexel';
    $path = $path['dirname'];
    $size = filesize($image);

    $metadatas[] = $name.".".$ext.$size;
}

sort($metadatas);

foreach($metadatas as $data){
    echo($data);
    echo "</br>";
}
*/

/**
 * @Author
 *  Jeong Han
 * @memo
 *  디렉토리 내 이미지 파일 이름 불러오기(디렉토리 핸들러)
 */
/*
$ext = array('.gif','.jpg','.png'); // 이미지 확장자 지정 
$path = './img/'; // 뒤에 경로 구분자 붙여주기 
if ( $dh = opendir($path) ) { 
    while ( ($read=readdir($dh))!==false ) 
    { 
        if ( !is_file($path.$read) || !in_array(strrchr($read,'.'),$ext) ) continue; 
        echo json_encode($read).'&nbsp'; // 이미지 파일만 출력 
    } 
    closedir($dh); 
}*/

/**
 * @Author
 *  Jeong Han
 * @date
 *  23.May.2018
 * @ref
 *  http://php.net/manual/en/function.exif-read-data.php
 * @memo
 *  image exif data read example
 */
/*
echo "test1(exif_read_data 옵션 : IFDO):\n";
$exif = exif_read_data('./img/ex1.png', 'IFD0');
echo $exif===false ? "No header data found.\n" : "Image contains headers\n";
$exif = exif_read_data('./img/ex1.png', 0, true);
echo "test2(exif_read_data 옵션 : 0, true):\n";
foreach ($exif as $key => $section) {
    foreach ($section as $name => $val) {
        echo "$name: $val\n";
    }
}*/

/**
 * @Author
 *  Jeong Han
 * @ref
 *  http://www.x2chi.com/55
 */

require_once "lib.php"; 

// 접근경로 확인 
if (!eregi($_SERVER['HTTP_HOST'], $_SERVER['HTTP_REFERER'])) Error("외부에서는 다운로드 받으실수 없습니다."); 


// 다운로드 방식을 구한다. 
$ext = array_pop(explode(".", $_GET['file_name'])); 

if ($ext=="avi" || $ext=="asf")         $file_type = "video/x-msvideo"; 
else if ($ext=="mpg" || $ext=="mpeg")   $file_type = "video/mpeg"; 
else if ($ext=="jpg" || $ext=="jpeg")   $file_type = "image/jpeg"; 
else if ($ext=="gif")                   $file_type = "image/gif"; 
else if ($ext=="png")                   $file_type = "image/png"; 
else if ($ext=="txt")                   $file_type = "text/plain"; 
else if ($ext=="zip")                   $file_type = "application/x-zip-compressed"; 

// 실제로 다운로드 받는다. 
//$ret = download_file( $_GET['file_name'], $_GET['file_micro'], "여기에 파일이 있는 디렉토리를 쓴다.", $file_type);
$ret = download_file( $_GET['file_name'], $_GET['file_micro'], "./img/*", $file_type);

if( $ret == 1 ) Error("지정하신 파일이 없습니다."); 
if( $ret == 2 ) Error("접근불가능 파일입니다. 정상 접근 하시기 바랍니다."); 

?>