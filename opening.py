import main
name=input('''Enter the cipher name('caesar_cipher,force_decrypt for caesar,
           atbash_cipher or Rail_Fence_cipher'): ''')

if name=="caesar_cipher":
    main.caesar_cipher()
elif name=="force_decrypt for caesar":
    main.force_decrypt()
elif name=="atbash_cipher":
    main.atbash_cipher()
elif name=="Rail_Fence_cipher":
    main.Rail_Fence_cipher()
else:
    print("You entered wrong cipher name. Try Again!!!")