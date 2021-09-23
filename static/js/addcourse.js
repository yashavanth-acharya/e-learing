
let tables=$('#example').DataTable({
    "processing": true,
    "pageLength": 10,
ajax: 'getcourse',

});





$("#addcourses").click(function () {

$("#addcourses").attr("disabled",true)
$("#addcourses").html('<i class="fa fa-spinner fa-spin"></i> Loading...')



$("#msg").empty()
$("#errormsg1").empty()

let name=$("#name").val()
let descriptions=$("#descriptions").val()
let icon=$('#image')[0].files;
let error1=0,error2=0,error3=0

if(name.length==0){
$("#coursename-error").html("Course name is required *")
$("#name").addClass("errorborder")
$("#name-error").addClass("errorlable")
error1=1
}else{
$("#coursename-error").html(" ")
$("#name").removeClass("errorborder")
$("#name-error").removeClass("errorlable")
error1=0
}

if(descriptions.length==0){
$("#course-description-error").html("Course descriptions is required *")
$("#descriptions").addClass("errorborder")
$("#descriptions-error").addClass("errorlable")
error2=1
}else{
    $("#course-description-error").html(" ")
    $("#descriptions").removeClass("errorborder")
    $("#descriptions-error").removeClass("errorlable")
    error2=0
}

if(icon.length==0){
    $("#iconerror").html("Course icon is required *")
    $("#imageUploaded").addClass("errorborder")
    $("#icon-error").addClass("errorlable")
    error3=1
    }else{

        let fileExtension = ['jpeg', 'jpg', 'png', 'gif'];
        if ($.inArray(String(icon[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
            $("#iconerror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
        }
        else{
            if(icon[0].size>1083743){
                $("#iconerror").html("Image size should be less than 1MB*")
                $("#imageUploaded").addClass("errorborder")
                $("#icon-error").addClass("errorlable")
                error3=1
            }else{
                $("#iconerror").html(" ")
                $("#imageUploaded").removeClass("errorborder")
                $("#icon-error").removeClass("errorlable")
                error3=0
            }
            
        }
                
    }

if(error1==0 && error2==0 && error3==0){
    $.ajax({
        method: "POST",
        url:"addcourse",
        data:{"name":name,"descriptions":descriptions,"icons":localStorage.getItem("courseicon")},
        success: function(data){
            
            
            if(data.error==0){
                echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  localStorage.removeItem("courseicon")
                  tables.ajax.reload();
                  $('#modal1').modal('toggle');
                  $("form").trigger('reset');
                  $("#msg").append(echo)
            }else{
                echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  $("#errormsg1").append(echo)

            }
            
            
            $("#addcourses").attr("disabled",false);
            $("#addcourses").html('Add')
           

        },
        error: function(message){
            echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>Done</strong> `+data.msg+`.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>`
              $("#errormsg1").append(echo)
              $("#addcourses").attr("disabled",false);
            $("#addcourses").html('Add')
        }
    })
}
 })
