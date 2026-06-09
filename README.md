# Professional Python - Sofftech

Bu repo, Sofftech eğitimi kapsamında Python programlama diline ait örnek kodları içermektedir.

## İçerik

### `datatypes/`

Python'da veri tipleri ve bellek yönetimine ilişkin örnekler:

| Dosya | Konu |
|---|---|
| `collectionsample.py` | `set`, `frozenset`, `defaultdict`, `Counter`, `namedtuple` kullanımı |
| `mutable-vs-immutable.py` | Değiştirilebilir ve değiştirilemez veri tipleri, güvenli kopyalama |
| `copy-and-deep-copy.py` | Sığ kopya (`copy`) ve derin kopya (`deepcopy`) farkları |
| `scope.py` | LEGB kural kapsamı, `global` ve `nonlocal` anahtar kelimeleri |

### `environments/`

| Dosya | Açıklama |
|---|---|
| `requirements.txt` | Projede kullanılan Python bağımlılıkları |

## Gereksinimler

Python 3.x ve aşağıdaki paketler:

```
requests==2.34.2
```

Bağımlılıkları yüklemek için:

```bash
pip install -r environments/requirements.txt
```

## Kullanım

İstediğiniz Python dosyasını doğrudan çalıştırabilirsiniz:

```bash
python datatypes/collectionsample.py
```
