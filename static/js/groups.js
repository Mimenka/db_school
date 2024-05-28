'use strict'

const data = {
    name: 'Название группы'
}
const group_add_btn = document.getElementById('group_add_btn')

group_add_btn.onclick = () => {
        fetch('http://localhost:5000/groups'), ({
            method: 'POST',
            headers: {
                'Content-Type': 'applications/json'
            },
            body: JSON.stringify(data),
    }).then(response => {
        if (!response.ok){
            throw new Error('Network response was not ok' + response.statusText)
        }
        return response.json()
    }).then(data => {
        console.log('Данные успешно сохранены в БД,', data)
    }).catch(error => {
        console.log('Ошибка при добавлении в БД,', error)
    })
}

