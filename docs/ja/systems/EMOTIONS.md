[简体中文](../../zh-CN/systems/EMOTIONS.md) | [English](../../en/systems/EMOTIONS.md) | [日本語](EMOTIONS.md)

# 感情システム

[システムの説明一覧](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

感情は、その発話区間の調子を表すもので、長期的な関係値ではありません。固定の 26 タグを使います。設定内のタグ名は通信上の識別子なので、翻訳せずそのまま記述してください。

| UI の色分け | タグ |
| --- | --- |
| ポジティブ／赤 | `Happy`, `Excited`, `Relaxed`, `Affectionate`, `Playful`, `Teasing`, `Smug` |
| ネガティブ／青 | `Sad`, `Crying`, `Pouting`, `Angry`, `Chiding`, `Nervous`, `Afraid`, `Shocked`, `Mocking`, `Sarcastic`, `Disagree` |
| 中立・混合／黄 | `Neutral`, `Tired`, `Sleepy`, `Confused`, `Curious`, `Think`, `Surprised`, `Shy` |

色は表示上の分類で、好感度の加点・減点ではありません。通信断や不明な状態が新しい感情タグになることもありません。

`Happy`、`Relaxed`、`Excited` は強さや状況が異なります。`Surprised` は、より強い衝撃を示す `Shocked` と同じではありません。親しみのある `Teasing` は `Mocking` や `Sarcastic` と区別します。`Chiding` は注意・叱責で、必ずしも `Angry` ほどの怒りを伴いません。`Curious` は本当の好奇心、`Think` は思案を示し、単に会話に参加している状態を指しません。`Tired` と `Sleepy` は疲れと眠気を区別します。

高好感度でもポジティブな反応の割合が固定されることはありません。気分、文脈、未解決の対立は引き続き影響します。感情タグだけで関係の変化を証明することもできません。

音声では区間ごとのタグから `emotion_tts.mapping` と `profiles` を通して参考音声を選びます。任意の参考音声がなければ `Neutral` に戻ります。主パッケージに Neutral WAV があるため、開始時に 26 種すべてを揃える必要はありません。重み、参考音声、環境によって表現力が異なり、タグどおりの音色を保証しません。[音声設定](../VOICE_SETUP.md#emotions-26)と[音声・字幕](SPEECH.md)を参照してください。
