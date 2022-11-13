$('select').on('change', function () {
    option = $("select option:selected").val();
     if (option == 1){
         $('[for="id_name"]').text('Название компании');
     }
     else{
         $('[for="id_name"]').text('Имя');
     }
 })
