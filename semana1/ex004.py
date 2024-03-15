while True:
    st = input('Digite sim ou não: ')

    if st.lower() == 'sim':
        print('Você digitou sim')
    elif st.lower() == 'não':
        print('Você digitou não')
    else:
        print(f'Você digitou {st}')
