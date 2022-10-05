# ScalesAPI - REST API for weights
## About
**ScalesAPI** реализует REST API интерфейс электронных весов. 
Поддерживает одновременную работу с несколькими весами. 
Предоставляет REST API интерфейс к электронным весам.

## Use Scenarios
1. Один или несколько серверов. На сервере работает ScalesAPI. 
Клиентом является web-приложение, реализованное например на Django Framework, Flask и др. 
Клиент получает результаты взвешивания от сервера(ов) весов через запросы к API.
2. Один или несколько серверов. На сервере работает ScalesAPI. 
Клиентом является web-страница. 
Клиент получает результаты взвешивания от сервера с помощью JavaScript Fetch API.

## JavaScript example
Пример HTML страницы с формой. Значение input элемента net_weight обновляется функцией update_wt() каждые 500 мс.

```html
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>ScalesAPI</title>
</head>
<body>
<form method="post">
    <div>
        <label for="id_net_weight">Масса</label>
        <input type="number" name="net_weight" id="id_net_weight">
    </div>
    <div>
        <button type="submit">Отправить</button>
    </div>
</form>

<script>
    const weight_url = "http://127.0.0.1:8000/weight/1";
    let weight_field = document.getElementById("id_net_weight");
    setInterval(update_wt, 500)
    function update_wt() {
        fetch(weight_url).then(function (response) {
            response.json().then(function (json) {
                weight_field.value = json.weight;
            });
        });
    }
</script>
</body>
</html>
```
## Requirements

- [Python](https://www.python.org/) v3.8
- [pyserial](https://pypi.org/project/pyserial/) v3.5
- [ScalesDriver](https://github.com/kr-aleksey/ScalesDriver.git)
- [uvicorn](https://pypi.org/project/uvicorn/) v0.18.3

## Install
```shell
cd path/ScaleAPI
python -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip  
python -m pip install -r requrements.txt
```

## Usage

**ScaleAPI** запускается командой:
```
uvicorn main:app --host 127.0.0.1 --port 8000
```

## License
***ScalesAPI*** - распространяется бесплатно "как есть", с обязательной ссылкой на [GitHub: kr-aleksey](https://github.com/kr-aleksey)
