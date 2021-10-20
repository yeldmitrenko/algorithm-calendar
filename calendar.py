def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = []
    previous_meeting_start, previous_meeting_end = sorted_meetings[0]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        if current_meeting_start <= previous_meeting_end:
            previous_meeting_end = max(current_meeting_end, previous_meeting_end)
        else:
            merged_meetings.append((previous_meeting_start, previous_meeting_end))
            previous_meeting_start, previous_meeting_end = current_meeting_start, current_meeting_end
    merged_meetings.append((previous_meeting_start, previous_meeting_end))

    return merged_meetings


def normalize_output(array):
    array = merge_ranges(array)
    time_block = 30
    time_start = 540
    text = "Team's work time: \n"
    for time in array:
        start = time_start + time[0] * time_block
        end = time_start + time[1] * time_block
        text += f"\t{start // 60:02d}:{start % 60:02d} - {end // 60:02d}:{end % 60:02d}\n"
    print(text)


if __name__ == '__main__':
    input_array = [(0, 2), (3, 4), (5, 10), (4, 12)]
    normalize_output(input_array)
