<html>
  <h1 align="center">ML-Inter-Face</h1>
  <h3 align="center">"プログラミング言語は書かず"に"モデルの構築やパラメータの調整"を体験してみよう！</h3>
  <a href="https://open.vscode.dev/paccho/ML-Inter-Face"><img src="https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc"></img></a>
  <h3>1. 概要</h3>
  <p>　ML-Inter-Faceは、ビジュアルプログラミングを活用してAIを開発できるサービスです。
     AIエンジニアを目指して「AIモデルをつくりたい！」と思っても、プログラミング言語が分からずに一歩を踏み出せない初学者は少なくありません。その課題を解決する一つの手段として、近年注目を集める生成AIがあります。<br>
     　たとえば、「このデータの〇〇を予測するAIをつくって」とプロンプトに入力するだけで、簡単にAIを構築できる便利な機能があります。しかし、その一方で、初学者が「仕組みは分からないけど、とりあえず作れた！」という状況に陥ることも少なくありません。私たちは、これを課題として捉えています。<br>
     　このような学び方では、AI開発に必要な基礎的な技術や知識が身に付かず、結果としてAIエンジニアとしての成長が妨げられるからです。確かに、プログラミング言語を学ぶことが大きなハードルとなるのは事実です。しかし、私たちはプログラミングはあくまで手段の一つであり、AI開発のプロセスを理解することが最優先だと考えています。プロセスを理解した後でプログラミングを学び始めても、遅すぎることはありません。そこで私たちが提案するのが、ML-Inter-Faceです。<br>
     　このサービスでは、「プログラミング言語を書かずにモデルの構築やパラメータ調整を繰り返し体験」することで、AI開発の知識を深めていくことができます。そして、体験を積み重ねる中で自然にプログラミング言語への理解も広がり、初学者が効率よく成長できる環境を提供します。<br>
     　ML-Inter-Faceは、初心者からAIエンジニアへの成長を支援する、次世代のAI開発プラットフォームを目指します。<br>
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
  <video src="https://github.com/user-attachments/assets/8beaf363-2dc2-4e51-a9bf-5263775c9607"></video>
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

  <h3>3. 技術スタック</h3>
  <img src="https://github.com/user-attachments/assets/da0527c1-1d5b-4433-9656-1d1ae9222cc0"></img>
  
  <h3>4. 今後の展開について</h3>
  <p>ML-Inter-Faceは初学者向けのサービスであるが、現在の機能では、ほぼ中級者に近い層がターゲットになっている。<br>そのため、さらに初学者に寄り添ったサービスへと改善するために、下記機能を実装したいと考えている。</p>
  <ul>
    <li>専門用語の説明、または文字を限りなく除外しビジュアルで表現</li>
    <li>学習レベル別チュートリアル</li>
    <li>使い方を質問できるチャットボット</li>
  </ul>
  <p>また、WEBアプリケーションとして提供するための準備も必要。</p>

</html>


