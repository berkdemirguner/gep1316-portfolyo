# Prompt Günlüğü ve Yapay Zekâ Kullanım Beyanı

## Kullanılan istemler

| İstemim | YZ ne yaptı? | Benim kontrolüm / yaptığım düzenleme |
|---|---|---|
| Python'da kullanıcıdan adını ve doğum yılını alan, yaşını hesaplayan ve kişiye özel karşılama mesajı veren bir program hazırla. Her satırı Türkçe yorumla açıkla. | `input()`, tür dönüşümü, yaş hesabı ve `print()` kullanan ilk program taslağını oluşturdu. | Kodun her adımının yönergedeki istekle eşleşmesi için satır açıklamaları ve kullanıcı girdileri gözden geçirilecek. |
| Doğum yılı bu yıldan büyükse uyarı vermek istiyorum. Kodu yazmadan önce hangi Python yapısının kullanılacağını açıkla. | `if` koşulunun ve `datetime.now().year` ile mevcut yılı almanın nasıl kullanılacağını açıkladı. | Programda gelecek yıl kontrolü `if` koşuluyla uygulandı; bu durum gelecek yıl girilerek test edildi. |
| Kullanıcı yıl yerine harf girerse veya boş ad girerse programın nasıl davranması gerektiğini öner. | `isdigit()` ile giriş kontrolü ve boş ad için varsayılan hitap önerdi. | Kodda sayısal olmayan yıl girişi engellendi; boş ad için “Arkadaşım” hitabı eklendi. |

## Test notu

Program örnek olarak `Deniz` adı ve `2000` doğum yılı ile çalıştırıldı. Ayrıca gelecekteki bir yıl ve sayısal olmayan yıl girdileriyle uyarı kontrolleri denendi. Yaş hesabı yalnızca yıl farkına dayalıdır; doğum gününün bu yıl geçip geçmediğini dikkate almaz.

## Yapay zekâ kullanım beyanı

- **Kullanılan YZ aracı:** ChatGPT (OpenAI)
- **Kullanma amacı:** README metnini düzenlemek, Python programı için ilk taslağı ve açıklamaları hazırlamak, hata kontrolü ve prompt günlüğü oluşturmak.
- **Kontrol ve sorumluluk:** Yapay zekâ tarafından üretilen içerik üzerinde kontrol ve test yapılmalıdır. Öğrenci, GitHub'a yüklemeden ve teslim etmeden önce kodu kendi bilgisayarında yeniden çalıştırmalı, içeriği anlamalı ve gerekli gördüğü düzeltmeleri yapmalıdır. Nihai çalışmanın doğruluğu ve akademik dürüstlüğünden öğrenci sorumludur.
- **Öğrencinin adı-soyadı:** Berk Demir Güner
- **Öğrenci numarası:** 2482965
- **Tarih:** 24.11.2026

## APA 7 kaynak gösterimi

OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com/
