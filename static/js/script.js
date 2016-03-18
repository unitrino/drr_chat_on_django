var old_val = "";
function select_avatar(sel_ava)
{
    if (old_val == sel_ava || old_val == "")
    {
        old_val = sel_ava;
        document.getElementById(sel_ava).className = "img_select_avatar";
        document.getElementById("hidden_avatar").value = sel_ava;
    }
    else
    {
        document.getElementById(sel_ava).className = "img_select_avatar";
        document.getElementById(old_val).className = "img_avatar";
        old_val = sel_ava;
        document.getElementById("hidden_avatar").value = sel_ava;
    }
}



