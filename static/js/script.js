var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 各プレーヤーの格納配列準備
const ytPlayer = [];

// Youtube再生判定用
let ytPlaying, ytStop, ytPlay;

function pushBtn() {
  var url1 = window.hogeLib.url1();
  alert(url1);
};

var url1 = window.hogeLib.url1();
var url2 = window.hogeLib.url2();
var url3 = window.hogeLib.url3();

  const ytData = [
    {
      id: url1, // youtube動画のID  pass.htmlからurl2を取得
      area: 'youtube1', // youtube動画を埋め込む場所
      pWidth: '200', // 動画の幅
      pHeight: '100' // 動画の高さ設定用
    },
    {
      id: url2, // youtube動画のID
      area: 'youtube2', // youtube動画を埋め込む場所
      pWidth: '200', // 動画の幅
      pHeight: '100' // 動画の高さ設定用
    },
    {
      id: url3, // youtube動画のID
      area: 'youtube3', // youtube動画を埋め込む場所
      pWidth: '200', // 動画の幅
      pHeight: '100' // 動画の高さ設定用
    }
  ];

  // 各プレーヤーの埋め込み
  function onYouTubeIframeAPIReady() {
    for (let n = 0; n < ytData.length; n++) {
      ytPlayer[n] = new YT.Player(ytData[n]['area'], {
        width: ytData[n]['pWidth'],
        height: ytData[n]['pHeight'],
        videoId: ytData[n]['id'],
        playerVars: {
          rel: 0,
          playsinline: 1
        },
        events: {
          onReady: function(evt) { // ここに動画再生の準備ができた時に実行したいscriptを記述
          },
          onStateChange: function(evt) { // ここに動画のステータスが変わった時に実行したいscriptを記述
            /* 複数再生させない制御 */
            // 各プレーヤーの状態確認
            let thisState = ytPlayer[n].getPlayerState();

            if (thisState === 1 && typeof ytPlaying === 'undefined') { // 初回再生時
              ytPlaying = n;
            } else if (thisState === 1 && ytPlaying !== n) { // 他が再生されてる時
              ytStop = ytPlaying;
              ytPlay = n;
            }

            // 同時再生があった場合、元々再生していた方を停止する
            if (typeof ytStop !== 'undefined' && ytStop !== '') {
              ytPlayer[ytStop].pauseVideo();
              ytStop = '';
            }

            // 現在再生中のプレーヤー番号を保存しておく
            if (typeof ytPlay !== 'undefined' && ytPlay !== '') {
              ytPlaying = ytPlay;
              ytPlay = '';
            }
          }
        }
      });
    }
  }

