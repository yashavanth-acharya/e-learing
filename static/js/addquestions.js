    
let tables=$('#example').DataTable({
    "processing": true,
    "pageLength": 10,
    ajax: 'addquestion',

});

$("#addquestion").click(function(){
    $("#errormsg1").empty();    
    let question=$("#Question").val();
    let Options1=$("#Options1").val();
    let Options2=$("#Options2").val();
    let Options3=$("#Options3").val();
    let Options4=$("#Options4").val();
    let answers=$("#answers").val();
    let error1=0,error2=0,error3=0,error4=0,error5=0,error6=0
    if(question.length==0){
        $("#Questionerror").html("Question is required *")
        $("#Question").addClass("errorborder")
        $("#Question-error").addClass("errorlable")
        error1=1
        }else{
        $("#Questionerror").html(" ")
        $("#Question").removeClass("errorborder")
        $("#Question-error").removeClass("errorlable")
        error1=0
        }

        if(Options1.length==0){
            $("#Options1error").html("Options 1 is required *")
            $("#Options1").addClass("errorborder")
            $("#Options1-error").addClass("errorlable")
            error2=1
            }else{
            $("#Options1error").html(" ")
            $("#Options1").removeClass("errorborder")
            $("#Options1-error").removeClass("errorlable")
            error2=0
            }


        if(Options2.length==0){
            $("#Options2error").html("Options 2 is required *")
            $("#Options2").addClass("errorborder")
            $("#Options2-error").addClass("errorlable")
            error3=1
            }else{
            $("#Options2error").html(" ")
            $("#Options2").removeClass("errorborder")
            $("#Options2-error").removeClass("errorlable")
            error3=0
            }

        if(Options3.length==0){
            $("#Options3error").html("Options 3 is required *")
            $("#Options3").addClass("errorborder")
            $("#Options3-error").addClass("errorlable")
            error4=1
            }else{
            $("#Options3error").html(" ")
            $("#Options3").removeClass("errorborder")
            $("#Options3-error").removeClass("errorlable")
            error4=0
            }

        if(Options4.length==0){
            $("#Options4error").html("Options 4 is required *")
            $("#Options4").addClass("errorborder")
            $("#Options4-error").addClass("errorlable")
            error5=1
            }else{
            $("#Options4error").html(" ")
            $("#Options4").removeClass("errorborder")
            $("#Options4-error").removeClass("errorlable")
            error5=0
            }
        if(answers.length==0){
            $("#answererror").html("Answers is required *")
            $("#answer").addClass("errorborder")
            $("#answer-error").addClass("errorlable")
            error6=1
            }else{
            $("#answererror").html(" ")
            $("#answer").removeClass("errorborder")
            $("#answer-error").removeClass("errorlable")
            error6=0
            }

            if(error1==0 && error2==0 && error3==0 && error4==0 && error5==0 && error6==0){
                data={
                    "Question":question,
                    "Options1":Options1,
                    "Options2":Options2,
                    "Options3":Options3,
                    "Options4":Options4,
                    "Answers":answers,
                }
                $.ajax({
                    method: "POST",
                    url:"addquestion",
                    data:data,
                    success: function(data){
                        
                        
                        if(data.error==0){
                            echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                                <strong>Done</strong> `+data.data+`.
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              </div>`
                              tables.ajax.reload();
                             // $('#modal1').modal('toggle');
                              $("form").trigger('reset');
                              $("#errormsg1").append(echo)
                        }else{
                            echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                                <strong>Done</strong> `+data.data+`.
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              </div>`
                              $("#errormsg1").append(echo)
            
                        }               
            
                    },
                    error: function(message){
                        echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <strong>Done</strong> `+data.msg+`.
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                          </div>`
                          $("#errormsg1").append(echo)
                    }
                })
            }



})