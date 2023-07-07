import psutil
import PySimpleGUI as sg

def get_network_traffic():
    stats = psutil.net_io_counters(pernic=True)
    return stats

def main():
    # Define the layout for the GUI
    layout = [
        [sg.Text('Network Traffic Monitor')],
        [sg.Output(size=(50, 10), key='-OUTPUT-')],
        [sg.Button('Start'), sg.Button('Stop'), sg.Button('Exit')]
    ]

    # Create the GUI window
    window = sg.Window('Network Traffic Monitor', layout)

    while True:
        event, values = window.read()

        # Exit the program if the window is closed or Exit button is clicked
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Start':
            window['-OUTPUT-'].update('Monitoring network traffic...\n')

            while True:
                try:
                    stats = get_network_traffic()
                    window['-OUTPUT-'].update(stats)  # Update the output with network traffic stats
                    sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)  # Show loading animation
                    sg.popup_animated(None)  # Hide loading animation
                except KeyboardInterrupt:
                    break

        if event == 'Stop':
            window['-OUTPUT-'].update('Network traffic monitoring stopped.\n')

    window.close()

if __name__ == '__main__':
    main()
