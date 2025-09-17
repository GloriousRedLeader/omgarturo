# ===============================================
# Imports
# ===============================================
from datetime import datetime, timedelta
import sys

# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-03-26
# Use at your own risk. 


# I DID NOT WRITE THIS SCRIPT!
# Credit goes to wherever this came from. 
# Im hosting for safekeeping.
# Also, it may or may not work. I forget. Good luck.
# Shared on IUO discord by Theavis on 8/2/2024.

class Puzzle:
    def __init__(self, timeout=400):
        self.skill = {'start': Player.GetSkillValue('Remove Trap'),
                      'now': Player.GetSkillValue('Remove Trap'),
                      'cap': Player.GetSkillCap('Remove Trap')}
        self.check_skill()
        self.messages = {
            'success': "You successfully disarm the trap",
            'fail': "You fail to disarm the trap and reset it"}
        self.dirs = {1: ("up", (-1, 0)),
                     2: ("right", (0, 1)),
                     3: ("down", (1, 0)),
                     4: ("left", (0, -1))}
        self.runs = {'total': 0, 'fails': 0, 'successes': 0}
        self.bau_list = get_bau_list()
        self.bau = self.get_bau()
        self.gump, self.size = -1, -1
        self.timeout = timeout
        self.start_time = self.reset_time()
        self.path, self.m_idx, self.matrix = self.reset()

    def get_bau(self):
        return next(self.bau_list)

    def reset_matrix(self):
        self.open_gump()
        self.m_idx = [1, 1]
        self.matrix = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        if self.size < 5:
            for p in range(7):
                self.matrix[5][p] = 1
                self.matrix[p][5] = 1
        if self.size < 4:
            for p in range(7):
                self.matrix[4][p] = 1
                self.matrix[p][4] = 1
        return self.m_idx, self.matrix

    def reset(self):
        self.path = []
        self.m_idx, self.matrix = self.reset_matrix()
        return self.path, self.m_idx, self.matrix

    def reset_time(self):
        self.start_time = datetime.now()
        return self.start_time

    def open_gump(self):
        timeout = 6500
        while True:
            self.gump, self.size = get_puzzle_gump_info()
            if self.gump > 0:
                break
            Player.UseSkill('Remove Trap')
            Target.WaitForTarget(timeout, False)
            Target.TargetExecute(self.bau)
            timeout = 500

    def get_matrix_pos(self, num):
        y, x = self.dirs[num][1]
        return y + self.m_idx[0], x + self.m_idx[1]

    def set_matrix_pos(self, num):
        self.m_idx = self.get_matrix_pos(num)
        self.matrix[self.m_idx[0]][self.m_idx[1]] = 1

    def valid_position(self, num):
        _ny, _nx = self.get_matrix_pos(num)
        return self.matrix[_ny][_nx] == 0

    def check_timeout(self):
        return timedelta.total_seconds(datetime.now() - self.start_time) > self.timeout

    def check_skill(self):
        if self.skill['now'] >= self.skill['cap']:
            Misc.SendMessage("Remove Trap Skill is in it's Cap. \r\nFinishing.", 0x95)
            sys.exit()

    def change_bau(self):
        self.bau = self.get_bau()
        Misc.Pause(500)
        Gumps.CloseGump(self.gump)

    def set_run_data(self, run_status):
        self.runs['total'] += 1
        if run_status == 'Success':
            self.runs['successes'] += 1
        else:
            self.runs['fails'] += 1
        self.skill['now'] = Player.GetSkillValue('Remove Trap')

    def print_run_data(self, state, message):
        t = {'Success': ('solve', 0x45), 'Fail': ('run', 0x20)}
        Misc.SendMessage(state + '! ' + str(self.size) + 'x' + str(self.size) + ' gump \r\n' + t[state][0] + ' time: ' +
                         str(datetime.now() - self.start_time).split(".")[0] + ' ' + message + '\r\n', t[state][1])
        Misc.SendMessage('runs: ' + str(self.runs['total']) + '\r\n' + 'successes: ' + str(self.runs['successes']) +
                         ', fails: ' + str(self.runs['fails']) + '\r\n', 0x95)
        Misc.SendMessage('Skill:\r\nstart: ' + str(self.skill['start']) + '\r\nnow: ' + str(self.skill['now']) +
                         '\r\ngain: ' + str(self.skill['now'] - self.skill['start']) + '\r\n', 0x39)

    def finish(self, state, message):
        self.set_run_data(state)
        self.print_run_data(state, message)
        self.check_skill()
        self.reset_time()
        self.reset()


def get_bau_list():
    rank = {2: ('2nd', 'one'), 3: ('3rd', 'two')}
    while True:
        bau_list = []
        for i in range(1, 4):
            msg = 'Target a circuit trap training kit.'
            if i > 1:
                msg = ('dispute solving: Target a ' + rank[i][0] + ' option circuit trap training kit in your range.' +
                       '\r\nJust hit ESC or target anything else if just ' + rank[i][1] + ' is enough.')
            bau = Items.FindBySerial(Target.PromptTarget(msg))
            if bau and bau.ItemID == 0xA393:
                bau_list.append(bau)
            else:
                break
        if bau_list:
            return circular(bau_list)
        else:
            Misc.SendMessage('is that a circuit trap training kit?')


def circular(args):
    while True:
        for element in args:
            yield element


def get_puzzle_gump_info():
    gump = Gumps.CurrentGump()
    gump_data = Gumps.GetGumpRawData(gump)
    if '1159005' in gump_data:
        midpoints = gump_data.count("9720")
        size = 5
        if 7 < midpoints < 23:
            size = 4
        if midpoints <= 7:
            size = 3
        return gump, size
    return -1, -1


def get_puzzle_gump():
    return get_puzzle_gump_info()[0]


def handle_response(puzzle, pos):
    Journal.Clear()
    for _ in range(0, 50):
        Misc.Pause(100)
        if Journal.Search(puzzle.messages['success']):
            puzzle.finish('Success', '')
            return 1
        if Journal.Search(puzzle.messages['fail']):
            previous = puzzle.path
            puzzle.reset()
            build_path(puzzle, previous)
            return -1
        if get_puzzle_gump() > -1:
            puzzle.path.append(pos)
            puzzle.set_matrix_pos(pos)
            return 0
    puzzle.finish('Fail', '| Gump response timed out. Probably no gump')
    return 0


def build_path(puzzle, path_buttons):
    for button in path_buttons:
        Gumps.SendAction(puzzle.gump, button)
        response = handle_response(puzzle, button)
        if response != 0:
            return response
    return 0


def remove_trap():
    puzzle = Puzzle()
    while True:
        attempt_result = 0
        for num_button in (2, 3, 4, 1):
            if puzzle.check_timeout():
                puzzle.finish('Fail', '| Something went wrong - timeout')
                break

            if not puzzle.valid_position(num_button):  # pass
                attempt_result = -1
                continue

            Misc.SendMessage("path = " + " ".join([puzzle.dirs[v][0] for v in puzzle.path]) +
                             " | trying " + puzzle.dirs[num_button][0], 0x60)

            attempt_result = build_path(puzzle, [num_button])
            if not attempt_result == -1:
                break
        if attempt_result == -1:
            puzzle.change_bau()
            puzzle.finish('Fail',
                          '| Something is wrong. Maybe someone else is using the same box? trying the next ' +
                          str(puzzle.bau))

remove_trap()