<html>
  <h1 align="center">ML-Inter-Face</h1>
  <h2 align="center">We can easy to make Machine Learning Model with GUI!</h2>
  <a href="https://open.vscode.dev/paccho/ML-Inter-Face"><img src="https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc"></img></a>
  <h3>1. 概要</h3>
  <p>ML-Inter-FaceはビジュアルプログラミングでAIを開発することができるサービスです。<br>
     AIモデルをつくりたい。でも、プログラミングができない。。。そんなことが初学者にはありがちです。<br>
     それを解決しているのが、近年話題の生成AI。<br>
     プロンプトに「このデータの〇〇を予測するAIをつくって」などをインプットすることで、「どう動いているかわからないけど、開発できた！」という運用ができます。大変便利です。<br>
     しかし、これこそ私たちが問題視している事例です。これを初学者の方がとると、成長することができないためです。<br>
     そこで私たちは、ユーザーがプログラミング言語に触れず簡単にAIモデルを構築できる。そして、成長できるサービスを提案します！
     </p>
  <h3>2. 機能紹介デモ</h3>
  <h4>2-1. ユーザーログイン</h4>
  <video src="https://github.com/user-attachments/assets/8901a439-bd87-46fe-be66-c028dba7d3c6" setRate=2></video>
  <p>ここではユーザーログインができます。</p>

  <h4>2-2. プロジェクトの作成</h4>
  <video src="https://github.com/user-attachments/assets/611b4cf8-ccc7-49a6-954f-f3485acf6690"></video>
  <p>ここではプロジェクトの作成ができます。<br>データセットとして画像フォルダ、csvファイルなどを読み込むことができます。<br>今回は画像認識を行います。</p>

  <h4>2-3. 読み込んだ画像の確認とデータ分割</h4>
  <video src="https://github.com/user-attachments/assets/751359ce-752c-405b-8275-4607a1579f9e"></video>
  <p>ここでは読み込んだ画像の確認とデータ分割を行います。<br>上のバーで「学習」「検証」「テスト」データの割合を調整できます。</p>

  <h4>2-4. モデル構築</h4>
  <video src="https://github.com/user-attachments/assets/603a4073-f85c-4a9a-a8f1-887447791286"></video>
  <p>ここではモデル構築を行います。<br>アルゴリズムを選択後、レイヤーブロックを使ってモデルを構築しましょう！<br>
     ワンクリックで左下の詳細パラメータ、ダブルクリックでレイヤーを削除できます。<br>
     また、自力でコーディングしモデル構築を行った場合は、動画内にあるように.pyファイル読み込むことでコードをブロックに変換することができます！<br></p>
  
  <h4>2-5. コンパイル</h4>
  <video src="https://github.com/user-attachments/assets/2a5b6faf-2651-4e50-93b7-b260609cd5ef"></video>
  <p>ここでは、損失関数などのパラメータを決めます。<br>さあ、残すは学習フェーズのみ！</p>

  <h4>2-6. 学習</h4>
  <video src="https://github.com/user-attachments/assets/b3d74e9f-dcbb-4b42-9d50-b417be52c429"></video>
  <p>ここでは、学習を行います。バッチ数とエポック数を設定し、trainをクリックすると学習が始まります。<br>画面右のほうのグラフには「コンパイル」フェーズで設定した関数を使って算出したスコアがリアルタイムで描かれます！<br>
     また、学習中にモデル構築画面に戻り、スコアを見ながら次に行う学習モデルの構築を考えることもできます！<br>
     なお、学習後のモデルはプロジェクトフォルダに自動保存されるようになっています！</p>
  
  <h4>2-7. その他機能</h4>
  <p>ここまで、画像認識を使ったデモをお見せしましたが、csvファイルから学習を行うこともできます。</p>
  <video src="https://github.com/user-attachments/assets/66a10790-6195-41e9-acdb-4cbc746d3597"></video>
  <p>前処理として、欠損値補完・説明変数の選択と目的変数の選択が可能です。（黄：説明変数　赤：目的変数）<br>
     学習フェーズでは代表的なアルゴリズムが用意されています。<br>
     また、学習後は、出力されるグラフから精度を確認することができます。</p>

  <h4>2-8. 更なる発展を望む方へ</h4>
  <video src="https://github.com/user-attachments/assets/d8e45a5a-85a1-4718-84a0-a9c81dd8810f"></video>
  <p>任意のレイヤーの重みを好きなように編集することが可能です。<br>
     モデルの重みが変わったとき、精度にどれほど影響がでるか気になる方はこの研究機能をぜひ使ってみてください。</p>

  <h4>3. 今後の展開について</h4>
  <p>ML-Inter-Faceは初学者向けのサービスであるが、現在のサービス内容ではほぼ中級者に近い方がターゲットになっている。<br>そのため、さらに初学者に寄り添ったサービスへと改善するために、下記機能を実装したいと考えている。</p>
  <ul>
    <li>専門用語の説明、または文字を限りなく除外しビジュアルで表現</li>
    <li>チュートリアル</li>
    <li>使い方を質問できるチャットボット</li>
  </ul>

</html>
































