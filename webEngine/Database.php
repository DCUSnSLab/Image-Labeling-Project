<?php  
    $connect = new mysqli('localhost', 'gkswjd9969', '13149508', 'tag_data');
    mysqli_set_charset($connect, "utf8"); //한글 인코딩 설정
    $query = "SELECT * FROM tag_metadata ORDER BY filename desc";
    $result = mysqli_query($connect, $query);  
?>
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta http-equiv="Content-Type" content="text/html" charset="utf-8">
    <title>Webslesson Tutorial | Import CSV File Data into MySQL Database using PHP & Ajax</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<body>
    <br />
    <br />
    <div class="container" style="width:900px;">
        <a href="Main.php">Home</a>
        <h2 align="center">Import CSV File Data into MySQL Database using PHP & Ajax</h2>
        <h3 align="center">Tag Data</h3>
        <br />
        <form id="upload_csv" method="post" enctype="multipart/form-data">
            <div class="col-md-3">
                <br />
                <label>Add More Data</label>
            </div>
            <div class="col-md-4">
                <input type="file" name="tag_file" style="margin-top:15px;" />
            </div>
            <div class="col-md-5">
                <input type="submit" name="upload" id="upload" value="Upload" style="margin-top:10px;" class="btn btn-info" />
            </div>
            <div style="clear:both"></div>
        </form>
        <br />
        <br />
        <br />
        <div class="table-responsive" id="tag_table">
            <table class="table table-bordered">
                <tr>
                    <th>파일 이름</th>
                    <th>파일 크기</th>
                    <th>파일 속성</th>
                    <th>Region 갯수</th>
                    <th>Region 종류 및 좌표값</th>
                    <th>태그</th>
                </tr>
                <?php
                while($row = mysqli_fetch_array($result)){            
                ?>
                <tr>
                    <td>
                        <?php echo $row["filename"]; ?>
                    </td>
                    <td>
                        <?php echo $row["file_size"]; ?>
                    </td>
                    <td>
                        <?php echo $row["file_attributes"]; ?>
                    </td>
                    <td>
                        <?php echo $row["region_count"]; ?>
                    </td>                    
                    <td>
                        <?php echo $row["region_shape_attributes"]; ?>
                    </td>
                    <td>
                        <?php echo $row["region_attributes"]; ?>
                    </td>
                </tr>
                <?php  
                }  
                ?>
            </table>
        </div>
    </div>
</body>

</html>
<script>
    $(document).ready(function () {
        $('#upload_csv').on("upload", function (e) {
            e.preventDefault(); //form will not submitted  
            $.ajax({
                url: "import.php",
                method: "POST",
                data: new FormData(this),
                contentType: false, // The content type used when sending data to the server.  
                cache: false, // To unable request pages to be cached  
                processData: false, // To send DOMDocument or non processed data file it is set to false  
                success: function (data) {
                    if (data == 'Error1') {
                        alert("Invalid File");
                    } else if (data == 'Error2') {
                        alert("Please Select File");
                    } else {
                        $('#tag_table').html(data);
                    }
                }
            })
        });
    });
</script>