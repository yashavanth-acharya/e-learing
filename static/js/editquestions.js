function editquestion(id){
    $.ajax({
        url:"editquestion",
        method:"GET",
        data:{"questionid":id},
        success:function(data){
            if(data.error==0){
              
            //   options=JSON.parse(JSON.stringify((data.data.options).replace("'", '"')))
            console.log()
            $("#editQuestion").val(data.data.question);
            $("#editOptions1").val(data.data.options.option1);
            $("#editOptions2").val(data.data.options.option2);
            $("#editOptions3").val(data.data.options.option3);
            $("#editOptions4").val(data.data.options.option4);
            $("#editanswers").val(data.data.answer);
              
            }
        }
    })
} 


$("#editquestion").click(function(){
    $("#errormsg1").empty();    
    let question=$("#editQuestion").val();
    let Options1=$("#editOptions1").val();
    let Options2=$("#editOptions2").val();
    let Options3=$("#editOptions3").val();
    let Options4=$("#editOptions4").val();
    let answers=$("#editanswers").val();
    let error1=0,error2=0,error3=0,error4=0,error5=0,error6=0
    if(question.length==0){
        $("#editQuestionerror").html("Question is required *")
        $("#editQuestion").addClass("errorborder")
        $("#editQuestion-error").addClass("errorlable")
        error1=1
        }else{
        $("#editQuestionerror").html(" ")
        $("#editQuestion").removeClass("errorborder")
        $("#editQuestion-error").removeClass("errorlable")
        error1=0
        }

        if(Options1.length==0){
            $("#editOptions1error").html("Options 1 is required *")
            $("#editOptions1").addClass("errorborder")
            $("#editOptions1-error").addClass("errorlable")
            error2=1
            }else{
            $("#editOptions1error").html(" ")
            $("#editOptions1").removeClass("errorborder")
            $("#editOptions1-error").removeClass("errorlable")
            error2=0
            }


        if(Options2.length==0){
            $("#editOptions2error").html("Options 2 is required *")
            $("#editOptions2").addClass("errorborder")
            $("#editOptions2-error").addClass("errorlable")
            error3=1
            }else{
            $("#editOptions2error").html(" ")
            $("#editOptions2").removeClass("errorborder")
            $("#editOptions2-error").removeClass("errorlable")
            error3=0
            }

        if(Options3.length==0){
            $("#editOptions3error").html("Options 3 is required *")
            $("#editOptions3").addClass("errorborder")
            $("#editOptions3-error").addClass("errorlable")
            error4=1
            }else{
            $("#editOptions3error").html(" ")
            $("#editOptions3").removeClass("errorborder")
            $("#editOptions3-error").removeClass("errorlable")
            error4=0
            }

        if(Options4.length==0){
            $("#editOptions4error").html("Options 4 is required *")
            $("#editOptions4").addClass("errorborder")
            $("#editOptions4-error").addClass("errorlable")
            error5=1
            }else{
            $("#editOptions4error").html(" ")
            $("#editOptions4").removeClass("errorborder")
            $("#editOptions4-error").removeClass("errorlable")
            error5=0
            }
        if(answers.length==0){
            $("#editanswererror").html("Answers is required *")
            $("#editanswer").addClass("errorborder")
            $("#editanswer-error").addClass("errorlable")
            error6=1
            }else{
            $("#editanswererror").html(" ")
            $("#editanswer").removeClass("errorborder")
            $("#editanswer-error").removeClass("errorlable")
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
                    url:"editquestion",
                    data:data,
                    success: function(data){
                        
                        
                        if(data.error==0){
                            echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                                <strong>Done</strong> `+data.data+`.
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              </div>`
                              tables.ajax.reload();
                             $('#modal2').modal('toggle');
                              $("form").trigger('reset');
                              $("#msg").append(echo)
                        }else{
                            echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                                <strong>Done</strong> `+data.data+`.
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              </div>`
                              $("#errormsg2").append(echo)
            
                        }               
            
                    },
                    error: function(message){
                        echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                            <strong>Done</strong> `+data.msg+`.
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                          </div>`
                          $("#errormsg2").append(echo)
                    }
                })
            }



})