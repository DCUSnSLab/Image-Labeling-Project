<?php
/**
 * @memo : list on files in directory
 * @ref : https://stackoverflow.com/questions/27083553/php-file-list-array-into-array-tree
 */

function scanpath($path) {
    $myscan = scandir($path);
    $tree=[];
    foreach($myscan as $entry) {
        //echo '<br>'.$entry;
        if($entry==='.' || $entry ==='..') {
            // do nothing
        } else  if(is_dir($path.'/'.$entry)) {
            // this is a folder, I will recurse
            $tree[$entry] = scanpath($path.'/'.$entry);
        } else {
            // this is a file or link. Value is file size
            $tree[$entry] = filesize($path.'/'.$entry);
        }
    }
    return $tree;
}
$scanresult=scanpath(__DIR__."../crawler/google-images-download/개/");
echo '<pre>';
print_r($scanresult);
echo '</pre>';
?>