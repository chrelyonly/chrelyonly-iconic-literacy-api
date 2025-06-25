from flask import Flask, request, jsonify
import ddddocr
import base64

app = Flask(__name__)
ocr = ddddocr.DdddOcr()


@app.route('/')
def index():
    return '欢迎使用验证码识别服务：POST /ocr/file 或 /ocr/base64'

# 1. 上传图片文件
@app.route('/ocr/file', methods=['POST'])
def ocr_file():
    if 'file' not in request.files:
        return jsonify({'error': '未检测到上传文件'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '文件名为空'}), 400

    image_bytes = file.read()
    result = ocr.classification(image_bytes)
    return jsonify({'result': result})

# 2. 上传 base64 字符串
@app.route('/ocr/base64', methods=['POST'])
def ocr_base64():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({'error': '未提供 image 字段（Base64 字符串）'}), 400

    base64_str = data['image']
    if base64_str.startswith('data:image'):
        base64_str = base64_str.split(',')[1]  # 去掉前缀

    try:
        image_bytes = base64.b64decode(base64_str)
    except Exception as e:
        return jsonify({'error': 'base64 解码失败', 'detail': str(e)}), 400

    result = ocr.classification(image_bytes)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
