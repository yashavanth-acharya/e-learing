
    $("input:checkbox:checked"). attr("checked", "");
    function showpassword() {
        let x = document.getElementById("oldpassword");
        let y = document.getElementById("password");

        if (x.type === "password") {
          x.type = "text";
          y.type = "text";

        } else {
          x.type = "password";
          y.type = "password";

        }
      }


$("#btn").click(function(){
    $("#msg").empty()
    $("#btn").html('<i class="fa fa-spinner fa-spin"></i> Loading...')
    $("#btn").attr("disabled",true)
    function showerror(tag,errortag){
        if(tag.val().length==0){
            errortag.html("Required *")
            tag.addClass("errorborder")
            return false
        }else{
            tag.removeClass("errorborder")
            return true
        }
    }

    function validate(tag,errortag){

      
        if(tag.val().length<8 || tag.val().length >32){
            errortag.html("Password should be at least 8/32 characters ")
            tag.addClass("errorborder")
            return false
            }
            else{
            tag.removeClass("errorborder")
            return true
            }


    }

    let oldpassword=$("#oldpassword")
    let newpassword=$("#password")
    let oldpassword_error=$("#oldpassword-error")
    let newpassword_error=$("#newpassword-error")

    oldpassword_error.html("")
    newpassword_error.html("")
    let error1=true,error2=true

    error1=showerror(oldpassword,oldpassword_error)
    error2=showerror(newpassword,newpassword_error)

    if(error1){
        error1=validate(oldpassword,oldpassword_error)
    }
    if(error2){
        error2=validate(newpassword,newpassword_error)
    }
    if(error1 && error2){
        $.ajax({
            url: "changepassword",
            method:"POST",
            data:$("form").serialize(),
            success:function(data){
                if(data.error==0){
                    echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.data+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      $("form").trigger('reset');
                     
                }else{
                    echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.data+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                }
                $("#msg").append(echo)
                $("#btn").html('Change password')
                $("#btn").attr("disabled",false)
            },
            error: function(data){
                $("#btn").html('Change password')
                $("#btn").attr("disabled",false)
            }
        })
    }else{
        $("#btn").html('Change password')
        $("#btn").attr("disabled",false)
    }
  
   


})
