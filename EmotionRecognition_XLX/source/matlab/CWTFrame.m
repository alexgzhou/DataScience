function Frame = CWTFrame(x)
    Frame = zeros(32, 32);
	for ch = 1:32;
        % Scale 7 to 38 have the most information and they selected db4 to do cwt
        coeff = cwt(x(ch, :), 7:38, 'db4');
        for s = 1:32;
            Frame(ch, s) = sqrt(sum(abs(coeff(s, :).*coeff(s, :))));
        end
    end
end
