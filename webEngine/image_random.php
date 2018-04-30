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
        //array_push($files,"<img src=\"img/".$filename."\">\n"); // 배열에 img태그 내용 삽입
        $files[] = $filename."/n";                                 // 배열에 파일 경로 삽입
    }
}
 
// 핸들 해제 
closedir($handle);
 
// 정렬, 역순으로 정렬하려면 rsort 사용
sort($files);

// 배열 내용 모두 출력
foreach($files as $data){
    json_encode($data);
    //echo($data);
    //echo "</br>";
}
?>