$("#brand1").on("change", function () {

  $("#model1").removeAttr("disabled");

  let brand = $("#brand1").val();

  $("#model1 option").hide();

  $("#model1 option[data-brand="+ brand +"]").show();

});

$("#model1").on("change", function () {

  $("#year1").removeAttr("disabled");

  let model = $("#model1").val();

  $("#year1 option").hide();

  $("#year1 option[data-model="+ model +"]").show();

});

$("#year1").on("change", function () {

    $("#brand2").removeAttr("disabled");

});


$("#brand2").on("change", function () {

  $("#model2").removeAttr("disabled");

  let brand = $("#brand2").val();

  $("#model2 option").hide();

  $("#model2 option[data-brand="+ brand +"]").show();

});

$("#model2").on("change", function () {

  $("#year2").removeAttr("disabled");

  let model = $("#model2").val();

  $("#year2 option").hide();

  $("#year2 option[data-model="+ model +"]").show();

});

$("#year2").on("change", function () {

  $("#form-btn").removeAttr("disabled");

});



