# Видеоплеер

Современный встроенный видеоплеер для вашего сайта. Плеер обладает стандартными кнопками управления, позволяющими воспроизводить/останавливать видео, включать/выключать звук, а также переходить в полноэкранный режим.

[Попробовать](https://yulia51188.github.io/video-pleer/)

![image](/demo/demo_image.png)

## Ресурсы

- [Библиотека для создания видеоплеера](https://github.com/devmanorg/video-player-jslib), использующая:
  - [jQuery](https://jquery.com/)
  - [Playable](https://wix.github.io/playable/)
- [Liveroad](http://livereload.com/) - отслеживание изменений в файлах для удобства разработки
- [Fontawesome](https://fontawesome.ru/get-started/) - набор шрифтов для иконок кнопок видеоплеера

## Разработчикам

Для запуска плеера на локальной машине:
- склонируйте репозиторий
- установите библиотеку `liveroad`:
```bash
$ pip install livereload
```
- запустите сервер `liveroad`:
```bash
$ python server.py 
[I 220218 10:22:18 server:335] Serving on http://127.0.0.1:5500
[I 220218 10:22:18 handlers:62] Start watching changes
[I 220218 10:22:18 handlers:64] Start detecting changes
```
- откройте в браузере указанную страницу [http://127.0.0.1:5500](http://127.0.0.1:5500)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
