import './app.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap.min.js"
// node_modules 디렉토리에있는 파일들을 위와 같은 상대경로를 사용하여 import할 수 있다.
import App from './App.svelte'

const app = new App({
  target: document.getElementById('app'),
})

export default app