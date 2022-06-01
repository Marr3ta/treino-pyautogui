import pyautogui
import time
pyautogui.PAUSE = 0.3

pyautogui.alert('Tire as maos do teclado e mouse!')

#excel
pyautogui.hotkey('win','9')
pyautogui.hotkey('ctrl','c')

#navegador 1
pyautogui.hotkey('win','5')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

#repetir a tarefa

for c in range(0,4):
    pyautogui.hotkey('ctrl','t')
    pyautogui.hotkey('win','9')
    pyautogui.press('esc')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('win','5')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

    #copiar de baixo

    pyautogui.hotkey('win','9')
    pyautogui.press('esc')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('win','5')

    pyautogui.hotkey('ctrl','t')

    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

    print('+1 salvo')