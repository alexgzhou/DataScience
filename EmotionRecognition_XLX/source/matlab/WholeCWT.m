% Introduction to the DEAP data
% data    40 x 40 x 8064  video/trial x channel x data
% labels  40 x 4  video/trial x label (valence, arousal, dominance, liking)

NUM_INTERVIEW = 32;
NUM_VIDEO = 40;
NUM_WINDOW = 63;
NUM_CHANNEL = 32;
SIZE_WINDOW = 60;

WholeX = zeros([32 * 40, 63, 32, 32]);
WholeY = zeros([1, NUM_INTERVIEW * NUM_VIDEO]);
for index_interview = 1:NUM_INTERVIEW;
    fprintf('loading s%.2d...\n', index_interview);
    info = load(sprintf('s%.2d.mat', index_interview));
    for index_video = 1:NUM_VIDEO;
        index_set = (index_interview - 1) * NUM_VIDEO + index_video;
        for index_window = 1:NUM_WINDOW;
            source_frame = info.data(index_video, 1:NUM_CHANNEL, (index_window - 1) * SIZE_WINDOW + 1: index_window * SIZE_WINDOW);
            source_frame = reshape(source_frame, [32, 60]);
            WholeX(index_set, index_window, :, :) = CWTFrame(source_frame);
        end
        WholeY(index_set) = info.labels(index_video, 1);
    end
end

% Normalization
for i = 1:(32);
    for j = 1:32;
        WholeX(:, :, i, j) = Normalize(WholeX(:, :, i, j));
    end
end

fprintf('Start Store the Transformed Data\n');
save 'CWTX_Normalized.mat' WholeX;
save 'CWTY_Normalzied.mat' WholeY;
