<?php  
/**
 * Superglobals : $_FILES
 * ['my_file']['name'] : Original Name of File Before It Was Uploaded
 * ref = http://www.phpforkids.com/php/php-forms-file-uploads.php
 */
$file = $_FILES['tag_file']['name'];
if(!empty($file))
{
    echo "fileread success";
    $connect = new mysqli('localhost', 'gkswjd9969', '13149508', 'tag_data');
    $output = '';
    $allowed_ext = array("csv");
    $extension = end(explode(".", $file));
    if(in_array($extension, $allowed_ext))
    {
        $file_data = fopen($_FILES['tag_file']['tmp_name'], 'r');
        fgetcsv($file_data);
        while($row = fgetcsv($file_data))
        {
            $filename = mysqli_real_escape_string($connect, $row[0]);
            $file_size = mysqli_real_escape_string($connect, $row[1]);
            $file_attributes = mysqli_real_escape_string($connect, $row[2]);
            $region_count = mysqli_real_escape_string($connect, $row[3]);
            $region_id = mysqli_real_escape_string($connect, $row[4]);
            $region_shape_attributes = mysqli_real_escape_string($connect, $row[5]);
            $region_attributes = mysqli_real_escape_string($connect, $row[6]);
            $query = "
            INSERT INTO tag_metadata
                (filename, file_size, file_attributes, region_count, region_id, region_shape_attributes, region_attributes)
                VALUES ('$filename', '$file_size', '$file_attributes', '$region_count', '$region_id', '$region_shape_attributes', '$region_attributes')
            ";
            mysqli_query($connect, $query);
        }
        $select = "SELECT * FROM tag_metadata ORDER BY filename DESC";
        $result = mysqli_query($connect, $select);
        $output .= '
            <table class="table table-bordered">
                <tr>
                    <th>파일 이름</th>
                    <th>파일 크기</th>
                    <th>파일 속성</th>
                    <th>Region 갯수</th>                        
                    <th>Region 종류 및 좌표값</th>
                    <th>태그</th>
                </tr>
        ';
        while($row = mysqli_fetch_array($result))
        {
            $output .= '
                <tr>
                    <td>'.$row["filename"].'</td>
                    <td>'.$row["file_size"].'</td>
                    <td>'.$row["file_attributes"].'</td>
                    <td>'.$row["region_count"].'</td>s                          
                    <td>'.$row["region_shape_attributes"].'</td>
                    <td>'.$row["region_attributes"].'</td>
                </tr>
            ';
        }
        $output .= '</table>';
        echo $output;
    }
    else
    {
        echo 'Error1';
    }
}
else
{
    echo "Error2";
}
?>  