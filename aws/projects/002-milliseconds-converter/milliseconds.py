def convert(millisec):
    if (not millisec.strip("- ").isdigit() or int(millisec) < 1):
        return False

    else:
        millisec = int(millisec)
        if millisec >= 1000:

            time = {}
            time["hour"] = millisec // 3600000
            millisec = millisec % (3600000)
            time["min"] = millisec // 60000
            millisec = millisec % (60000)
            time["sec"] = millisec // 1000
            format_text = ""
            for i, j in time.items():
                if j != 0:
                    format_text += f"{j} {i}/s "
            return format_text
        else:
            return f"just {millisec} millisecond/s\n"