$("#addtopicdocument").click(function(){

    $("#addtopicdocument").attr("disabled",true)
    $("#addtopicdocument").html('<i class="fa fa-spinner fa-spin"></i> Loading...')
    $("#errormsg1").empty()
  
    let topicname=$("#topicname").val()
    let document=$('#document')[0].files;
  
    let error1=0,error2=0;
  
    if(topicname.length==0)
    {
    
        $("#topicname-error").html("Topic name is required *")
        $("#topicname").addClass("errorborder")
        $("#topicname-error").addClass("errorlable")
        error1=1
    
    }else{
    
        $("#topicname-error").html(" ")
        $("#topicname").removeClass("errorborder")
        $("#topicname-error").removeClass("errorlable")
        error1=0
    }
    
    if(document.length==0){
  
      $("#documenterror").html("Document is required *")
      $("#document").addClass("errorborder")
      $("#document-error").addClass("errorlable")
      error3=1
  
      }else{
  
          let fileExtension = ['pdf'];
          if ($.inArray(String(document[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
              $("#documenterror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
          }
          else{
              if(document[0].size>1083743){
  
                  $("#documenterror").html("Image size should be less than 1MB*")
                  $("#document").addClass("errorborder")
                  $("#document-error").addClass("errorlable")
                  error3=1
  
              }else{
  
                  $("#documenterror").html(" ")
                  $("#document").removeClass("errorborder")
                  $("#document-error").removeClass("errorlable")
                  error3=0
  
              }
              
          }
                  
      }
  
      if(error1==0 && error2==0){
        data={
            "topicname":topicname,
            "documents":localStorage.getItem("topicdocuments")
        }
    
        $.ajax({
            method: "POST",
            url:"document",
            data:data,
            success: function(data){
                if(data.error==0){
                    echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.msg+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      localStorage.removeItem("topicdocuments")
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
                
                $("#addtopicdocument").attr("disabled",false)
                $("#addtopicdocument").html('Add')
               
    
            },
            error: function(message){
                echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  $("#errormsg1").append(echo)
                  $("#addtopicdocument").attr("disabled",false)
                  $("#addtopicdocument").html('Add')
            }
        })
    }
  })