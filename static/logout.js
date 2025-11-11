function logout() {
    if(confirm("Вы уверены что хотите выйти?")) {
        window.location.replace(`${window.location.origin}/logout/`)
    }
}