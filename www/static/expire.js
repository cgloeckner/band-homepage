function check_expire() {
    const today = Date.now()
    const elements = document.getElementsByClassName('may_expire')

    for (const element of elements) {
        const expire_string = element.getAttribute('expire')
        const expire_date = Date.parse(expire_string)
        if (expire_date < today) {
            element.remove()
        }
    }
}
