from django import forms
from .models import BarangWishlist

# komponen halaman form
class WishlistForm(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']