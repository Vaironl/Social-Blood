function searchFunction() {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById('searchRequestInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("requestUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        div = li[i].getElementsByClassName("location")[0];
        if (div.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}