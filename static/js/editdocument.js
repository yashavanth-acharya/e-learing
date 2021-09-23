function editdocuments(id){
    $("#errormsg2").html("Loading....")
    $("#edittopicdocument-btn").attr("disabled",true)
    $.ajax({
        url:"editdocuments",
        method:"GET",
        data:{"id":id},
        success:function(data){
            if(data.error==0){

              localStorage.setItem("documentid",id)
              $("#edittopicname").val(data.data[0][0])
              if(data.data[0][1]){
                localStorage.setItem("edittopicdocuments",data.data[0][1])
              }
            $("#errormsg2").html("")
            $("#edittopicdocument-btn").attr("disabled",false)
            }
        }
    })

}


$("#edittopicdocument-btn").click(function(){

    $("#edittopicdocument-btn").attr("disabled",true)
    $("#edittopicdocument-btn").html('<i class="fa fa-spinner fa-spin"></i> Loading...')
    $("#editerrormsg1").empty()
  
    let topicname=$("#edittopicname").val()
    let document=$('#editdocument')[0].files;
  
    let error1=0,error2=0;
  
    if(topicname.length==0)
    {
    
        $("#edittopicname-error").html("Topic name is required *")
        $("#edittopicname").addClass("errorborder")
        $("#edittopicname-lable").addClass("errorlable")
        error1=1
    
    }else{
    
        $("#edittopicname-error").html(" ")
        $("#edittopicname").removeClass("errorborder")
        $("#edittopicname-lable").removeClass("errorlable")
        error1=0
    }
    
    if(document.length!=0){  
          let fileExtension = ['pdf'];
          if ($.inArray(String(document[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
              $("#editdocumenterror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
          }
          else{
              if(document[0].size>1083743){
  
                  $("#editdocumenterror").html("Image size should be less than 1MB*")
                  $("#editdocument").addClass("errorborder")
                  $("#editdocument-error").addClass("errorlable")
                  error2=1
  
              }else{
  
                  $("#editdocumenterror").html(" ")
                  $("#editdocument").removeClass("errorborder")
                  $("#editdocument-error").removeClass("errorlable")
                  error2=0
  
              }
              
          }
                  
      }
  
      if(error1==0 && error2==0){
        data={
            "topicname":topicname,
            "documents":localStorage.getItem("edittopicdocuments"),
            "id":localStorage.getItem("documentid")
        }
    
        $.ajax({
            method: "POST",
            url:"editdocuments",
            data:data,
            success: function(data){
                if(data.error==0){
                    echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.msg+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      localStorage.removeItem("edittopicdocuments")
                      localStorage.removeItem("documentid")
                      tables.ajax.reload();
                      $('#modal2').modal('toggle');
                      $("form").trigger('reset');
                      $("#msg").append(echo)
                }else{
                    echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.msg+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      $("#errormsg2").append(echo)
                }
                
                $("#edittopicdocument-btn").attr("disabled",false)
                $("#edittopicdocument-btn").html('Update')
               
    
            },
            error: function(message){
                echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  $("#errormsg2").append(echo)
                  $("#edittopicdocument-btn").attr("disabled",false)
                  $("#edittopicdocument-btn").html('Update')
            }
        })
    }else{
        $("#edittopicdocument-btn").attr("disabled",false)
        $("#edittopicdocument-btn").html('Update')  
    }
  })